# $NetBSD$

DISTNAME=	nbclassic-1.0.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=n/nbclassic/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/nbclassic/
COMMENT=	Jupyter web applications for multiple programming languages
LICENSE=	modified-bsd

DEPENDS+=	${PYPKGPREFIX}-jupyter_packaging>=0.9:../../devel/py-jupyter_packaging
DEPENDS+=	${PYPKGPREFIX}-jupyter_server>=1.17.0:../../pkgsrc_myownpkgs/py-jupyter_server
DEPENDS+=	${PYPKGPREFIX}-babel>0:../../devel/py-babel
DEPENDS+=	${PYPKGPREFIX}-notebook_shim>=0.1.0:../../pkgsrc_myownpkgs/py-notebook_shim

PYTHON_VERSIONS_INCOMPATIBLE=	27

.include "../../graphics/hicolor-icon-theme/buildlink3.mk"
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
