# $NetBSD$

DISTNAME=	accessible_pygments-0.0.5
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/accessible-pygments/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/Quansight-Labs/accessible-pygments
COMMENT=	A collection of accessible pygments styles
LICENSE=	modified-bsd

PYTHON_VERSIONS_INCOMPATIBLE=	27 37 38

DEPENDS+=	${PYPKGPREFIX}-pygments>=1.5:../../textproc/py-pygments
DEPENDS+=	${PYPKGPREFIX}-hatchling>=0:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-hatch-fancy-pypi-readme>=0:../../devel/py-hatch-fancy-pypi-readme
DEPENDS+=	${PYPKGPREFIX}-hatch-vcs>=0:../../devel/py-hatch-vcs

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
