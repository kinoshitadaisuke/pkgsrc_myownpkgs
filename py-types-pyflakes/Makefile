# $NetBSD$

DISTNAME=	types-pyflakes-3.0.0.4
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=t/types-pyflakes/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/python/typeshed
COMMENT=	Typing stubs for pyflakes
LICENSE=	apache-2.0

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-flakes>=2.1.1:../../devel/py-flakes

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
