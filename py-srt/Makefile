# $NetBSD$

DISTNAME=	srt-3.5.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/srt/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/cdown/srt
COMMENT=	A tiny library for parsing, modifying, and composing SRT files
LICENSE=	mit

USE_LANGUAGES=	# none

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	( \
	${MV} srt srt-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} srt-deduplicate srt-deduplicate-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} srt-fixed-timeshift srt-fixed-timeshift-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} srt-linear-timeshift srt-linear-timeshift-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} srt-lines-matching srt-lines-matching-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} srt-mux srt-mux-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} srt-normalise srt-normalise-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} srt-play srt-play-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} srt-process srt-process-${PYVERSSUFFIX} || ${TRUE}; \
	)

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
