# $NetBSD$

GITHUB_PROJECT=	rebound
DISTNAME=	3.28.4
GITHUB_TAG=	refs/tags/${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_GITHUB:=hannorein/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/hannorein/rebound/
COMMENT=	An open-source multi-purpose N-body code
LICENSE=	gnu-gpl-v1 OR gnu-gpl-v2 OR gnu-gpl-v3

DEPENDS+=	${PYPKGPREFIX}-ipywidgets>=0:../../www/py-ipywidgets

TEST_DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib

BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=0

WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

.include "../../math/py-numpy/buildlink3.mk"
# TODO: Migrate MASTER_SITES to MASTER_SITE_PYPI
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
